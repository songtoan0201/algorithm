import * from "module";

var ironman = {
  name: "Tony Stark",
  alias: "Iron Man"
};
var avengers_array = [
  {
    name: "Tony Stark",
    alias: "Iron Man",
    ability: "flight"
  },
  {
    name: "Bruce Banner",
    alias: "The Incredible Hulk",
    ability: "superhuman strength"
  },
  {
    name: "Steve Rogers",
    alias: "Captain America",
    ability: "superhuman strength"
  },
  {
    name: "Clint Barton",
    alias: "Hawkeye",
    ability: "superior hand-eye coordination"
  },
  {
    name: "Thor Odinson",
    alias: "Thor",
    ability: "teleportation"
  },
  {
    name: "Natasha Romanova",
    alias: "Black Widow",
    ability: "espionage"
  }
];

// .each()
_.each(ironman, function(value, key) {
  alert(key + ": " + value);
});

// .map()
// var avengersAssemble = _.map(avengers_array, function (avenger) {
//     return avenger;
// });
// console.log(avengersAssemble);

// // .pluck()
// var avengerNames = _.pluck(avengers_array, 'name');
// console.log(avengerNames);

// .where()
var superhumanStrengthAvengersArray = _.where(avengers_array, {
  ability: "superhuman strength"
});
console.log(superhumanStrengthAvengersArray);
// .findWhere()
var superhumanStrengthAvenger = _.findWhere(avengers_array, {
  ability: "superhuman strength"
});
console.log(superhumanStrengthAvenger);
// .filter()
var superhumanStrengthAvengers = _.filter(avengers_array, function(avenger) {
  return avenger.ability == "superhuman strength";
});
console.log(superhumanStrengthAvengers);
// .sortBy()
var sortedAvengerNames = _.sortBy(avengers_array, "name");
console.log(sortedAvengerNames);

// .last() or .first()... does exactly what you think
var firstAvenger = _.first(avengers_array); // returns the first value in an array
var lastTwoAvengers = _.last(avengers_array, 2); // The optional second parameter allows for additional values to be returned, but when specified, comes back as an array

// .range()
var newArray = _.range(0, 10); // returns an array with the values from argument1 (inclusive) to argument2 (exclusive)

// .defaults()
var almostAvenger = {
  name: "John Q. Public",
  alias: "John Q"
};
_.defaults(almostAvenger, {
  name: "Need a Real Name",
  alias: "Need a Superhero Name",
  abilities: "Need Superhero Abilities"
});
