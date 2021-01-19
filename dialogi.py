
def dialog_1(mapa_1, plecak_bohatera):
    if "zardzewialy_klucz" in plecak_bohatera:
        print("posiada klucz")
        print("moge dzieki niemu otworzyc drzwi")
        mapa_1[4][5] = " "
        plecak_bohatera.remove("zardzewialy_klucz")
        return mapa_1
    else:
        print("przynies mi klucz a bede mogl otworzyc drzwi")

def dialog_2(plecak_bohatera):
    print("posiadam zwyczajny klucz, wymienie sie z toba w zamian za ksiege czarow")
    print("czy chcesz dokonac wymiany?")
    if input() == "tak":
        if "ksiega_czarow" in plecak_bohatera:
            plecak_bohatera.append("zwyczajny_klucz")
            plecak_bohatera.remove("ksiega_czarow")

        else:
            print("nie posiadasz ksiegi czarow, przynies mi ja na wymiane")
    else:
        print("w takim wypadku zegnaj, do zobaczenia pozniej")


def dialog_3(zycie):
    print("nie podchodz do mnie!")
    zycie = zycie[:-1]
    zycie = zycie[:-1]