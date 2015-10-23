# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
Tag.create(tag_name: "Magic: The Gathering", photo_url: "magic.jpeg")
Tag.create(tag_name: "Backgammon", photo_url: "backgammon.jpeg")
Tag.create(tag_name: "Cards Against Humanity", photo_url: "cards_against_humanity.png")
Tag.create(tag_name: "Poker", photo_url: "poker.jpeg")
Tag.create(tag_name: "Mahjong", photo_url: "mahjong.jpeg")
Tag.create(tag_name: "Dungeons & Dragons", photo_url: "dungeons_and_dragons.jpeg")
Tag.create(tag_name: "Catan", photo_url: "settlers_of_catan.jpeg")
Tag.create(tag_name: "Scrabble", photo_url: "scrabble.jpeg")
Tag.create(tag_name: "Chess", photo_url: "chess.jpeg")