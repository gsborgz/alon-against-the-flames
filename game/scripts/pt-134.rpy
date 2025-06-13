label part134:

    "O ônibus percorre as estradas da zona rural. De início, o interior do veículo é sufocante e seu estô mago se embrulha a cada curva da estrada."
    "No en tanto, o motorista abre a janela e, mudando de as sento, você encontra um local onde a brisa atinge seu rosto."
    "Você logo relaxa na jornada, observando as pequenas e pitorescas aldeias pelas quais o ônibus passa."
    "Uma mulher encorpada entra no ônibus em um povoado e então acena polidamente para você. Ela desce no vilarejo seguinte."
    "A estrada sobe um pouco, passando por mil harais e pomares. As folhas estão mudando de cor e as árvores estão vivas com vermelhos e dourados gloriosos."
    "Você está começando a cochilar quando o condutor faz uma curva brusca em alta velocidade."
    "Agora você deve fazer um teste de DES. Os testes em Chamado de Cthulhu possuem 3 níveis de dificuldade: [difficultyText['normal']], [difficultyText['hard']] e [difficultyText['extreme']]."
    "Essa dificuldade determina o valor máximo que você precisa obter em um dado de 100 lados (1D100)."
    "Para um teste [difficultyText['normal']], você deve obter um valor igual ou abaixo do valor do atributo sento testado."
    "Para um teste [difficultyText['hard']], você deve obter um valor igual ou abaixo de metade do valor do atributo sento testado."
    "E para um teste [difficultyText['extreme']], você deve obter um valor igual ou abaixo de um quinto do valor do atributo sento testado."
    "Agora faça um teste ([difficultyText['normal']]) de Destreza [player.getAttrValuesText(player.attributes.DEX)]."

    $ result = dice.rollD100(1)

    if player.testAttribute(player.attributes.DEX, result, 'normal'):
        "Agora faça um teste ([difficultyText['normal']]) de Destreza [player.getAttrValuesText(player.attributes.DEX)].\nResultado: {color=#05df72}[result]{/color}"

        call part261
    else:
        "Agora faça um teste ([difficultyText['normal']]) de Destreza [player.getAttrValuesText(player.attributes.DEX)].\nResultado: {color=#fb2c36}[result]{/color}"

        call part59
