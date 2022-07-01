function bottleSong() {

  function saySong(beers = 99) {
    if (beers === 2) {
      return console.log(`2 bottles of beer on the wall, 2 bottles of beer.
      Take one down and pass it around, 1 bottle of beer on the wall.
      1 bottle of beer on the wall, 1 bottle of beer.
      Take one down and pass it around, no more bottles of beer on the wall.
      No more bottles of beer on the wall, no more bottles of beer.
      Go to the store and buy some more, 99 bottles of beer on the wall.`)
    } else {
      console.log(`${beers} bottles of beer on the wall, ${beers} bottles of beer.  
      Take one down and pass it around, ${beers - 1} bottles of beer on the wall.`)
      saySong(beers - 1)
    }
  }

  return saySong()

};
bottleSong();
