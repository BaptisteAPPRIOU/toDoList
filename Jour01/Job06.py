Capital = 10000
Taux = 50
Rendement = Capital*(1+Taux/100)
float(Rendement)
Gain = Rendement - Capital
print("Le gain est de : ",Gain,", et le taux est de : ",Taux,"%")
Capital = Rendement + 5000
Taux += 2
Rendement = Capital*(1+Taux/100)
Gain = Rendement - Capital
print("Le nouveau gain est de : ",Gain,", et le taux est de : ",Taux,"%")
Capital = Rendement * 0.9
Taux -= 1
Rendement = Capital*(1+Taux/100)
Gain = Rendement - Capital
print("Le montant final de l'investissement est de : ",Rendement," et le nouveau gain est de : ",Gain)