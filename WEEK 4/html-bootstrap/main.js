function randomNumber() {
    return Math.floor(Math.random() * 898)
}

function getPokemon() {
    let id = randomNumber()
    axios.get(`https://pokeapi.co/api/v2/pokemon/${id}/`).then((info) => {
        let type = ''
       
        let pokePics = []
        type = info.data.types[0].type.name
        pokePics = [info.data.sprites.front_default]
        console.log(pokePics)

        for (let i = 1; i < 898; i++) {
            console.log('GETTING FOR LOOP', pokePics)
            if (pokePics.length > 6) {
                console.log('FINISHED')
                return pokePics
            }
            axios.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber()}/`).then((otherPokemon) => {
                otherType = otherPokemon.data.types[0].type.name
                if (otherType === type) {
                    pokePics.push(otherPokemon.data.sprites.front_default)
                    console.log(pokePics)
                } else {
                    console.log("diff type")
                }
            }).catch(function (error) {
                console.log('There is an error')
            })
        }
    })
    for (let i = 1; i < 898; i++) {
        console.log('GETTING FOR LOOP', pokePics)
        if (pokePics.length > 6) {
            console.log('FINISHED')
            return pokePics
        }
        axios.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber()}/`).then((otherPokemon) => {
            otherType = otherPokemon.data.types[0].type.name
            if (otherType === type) {
                pokePics.push(otherPokemon.data.sprites.front_default)
                console.log(pokePics)
            } else {
                console.log("diff type")
            }
        }).catch(function (error) {
            console.log('There is an error')
        })
    }

    // for (let i = 1; i < 1128; i++) {
    //     if (pokePics.length > 6) {
    //         return pokePics
    //     }

    //     let pokeType = ''
    //     let pokePic = ''

    //     axios.get(`https://pokeapi.co/api/v2/pokemon/${i}/`).then((info) => {
    //         pokeType = info.data.types[0].type.name
    //         pokePic = info.data.sprites.front_default
    //         console.log(pokeType)
    //         console.log(pokePic)

    //     })
    // }

    // console.log(pokePics)
}