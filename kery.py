import random


class Kelly:
    """モンテカルロ法によるケリーの公式のシミュレーション。
    v = Kelly(勝率, オッズ[, 試行回数, 総資金])
    で実行する。デフォルトでは試行回数は30回、総資金は10,000の設定
    """

    def __init__(self, prob, odds, n=30, money=10000):
        """初期化。最後に自動で走らせてる。"""
        self.count = n                  # 試行回数。デフォルトでは30に設定。
        self.prob = prob                # 確率(と言うより閾値)。
        # 0〜1の乱数を生成して、prob以下の場合「当たり」判定。
        self.odds = odds                # オッズ。賭け金
        self.money = money              # 所持金。初期値はデフォルトで10,000円に設定
        self.total_bet = 0              # 総投資金。トータルでいくら賭けたのか、と言うのは大事な指標。
        self.total_refund = 0           # 総払い戻し金。これも大事な指標

        self.test()                     # ここで自動でtest()メソッドを呼び出している

        # 収支計算。デフォルト引数は影響を受けないので、純利益はその値を利用して計算。
        print("総資金額:" + str(self.total_bet) + "円", "総払い戻し金額:" +
              str(self.total_refund), "円", "\n純利益:" + str(self.money - money)+"円")

    def optimal_f(self):
        """ケリーの公式。オプティマルfと言うのは別称
        数学的には
        (オッズ×確率 - 1) ÷ (オッズ - 1)
        を返り値にしているだけである"""
        return (self.odds * self.prob - 1) / (self.odds - 1)

    def luck(self):
        """確率計算。乱数を用いる。
        ロジックは乱数を発生させ、それが閾値(self.prob)より小さければ当たりと判定、
        そうじゃなければハズレと判定させる。
        True/Falseを返しているのは、Pythonの条件式に喰わせる際にこの方が便利だからである。
        (つまりif True => 実行、状況を作る為)"""
        val = random.random()
        if val <= self.prob:
            return True
        else:
            return False

    def test(self):
        """モンテカルロ法の心臓部。基本ループを回して結果を記録していくだけである。
        """
        for i in range(self.count):     # カウンターはiでself.countからリストイテレータを回す。
            # 投資金算出。基本的には、オプティマルfに現時点での総資金を賭ければ投資金になる。
            bet = round(self.optimal_f() * self.money / 100) * 100
            # 投資金算出したら「総投資金」に加算していく
            self.total_bet += bet
            # サイコロ。lackメソッドを呼び出して、結果を代入してる。
            dice = self.luck()
            # オプティマルfが0以下 = 回収期待値が0以下で儲からないのが自明なので、この場合は賭け中止。
            # あるいは賭け金が0、ってのもシミュレーションの性質上ダメなのでナシでキマリ。
            if self.optimal_f() <= 0 or bet == 0:
                print("賭けを中止します")
                return
            elif self.money <= 100:
                print("破産しました")
                return
            # dice = Trueの場合、「的中」を意味する。
            elif dice:
                print("%d回目 : 的中! 賭け金は%d円、" % (i + 1, bet),)
                refund = self.odds * bet  # 払戻金計算。オッズ×投資金になる
                self.total_refund += refund  # 総投資金に追加。記録の為。
                self.money = self.money + refund - bet  # 所持金は所持金に払戻金を足して、投資金を引いたもの。
                print("所持金は%d円です" % self.money)
            # 残りはハズレの場合。
            else:
                print("%d回目 : 残念! 賭け金は%d円、" % (i + 1, bet),)
                self.money -= bet       # 総資金から賭け金を引く。
                print("所持金は%d円です" % self.money)


if __name__ == '__main__':
    Kelly(0.7, 1)
