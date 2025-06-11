define busdriver = Npc("Motorista", "busdriver", "#ffffff")

label part263:

    "Dois jovens carrancudos saem do ônibus. Um deles o olha de alto a baixo antes de seguir seu caminho. O motorista também desce, olhando para você antes de atravessar a rua e entrar na tabacaria."
    "Quando ele volta, está enrolando um cigarro entre os dedos amarelados. Ele dá uma última volta no papel e o examina enquanto pega uma caixa de fósforos." 
    "É um homem magro com cinquenta e poucos anos, vestido com uma camisa manchada que traz o emblema da companhia de ônibus. No entanto, possui olhos afiados acima de suas olheiras."

    $ busdriver.enable()
    $ busdriver.say("Vai pra onde?")
    $ busdriver.disable()

    "Você mostra seu bilhete para Ossipee. De lá, você fará conexão em Rochester e Portsmouth, antes da linha costeira para Newburyport e, finalmente, chegará em Arkham."
    "Você deve conseguir pagar uma passagem de trem para pelo menos parte do caminho; caso contrário, esta será a primeira de muitas longas viagens de ônibus."

    $ busdriver.enable()
    $ busdriver.say("Mmm-hm.")
    $ busdriver.disable()

    "O motorista risca o fósforo e acende o cigarro. A ponta brilha avermelhada quando ele traga. Então ele sopra a fumaça e aponta para o fundo do ônibus."

    $ busdriver.enable()
    $ busdriver.say("O bagageiro fica ali em cima.")
    $ busdriver.disable()

    call part8

    return
