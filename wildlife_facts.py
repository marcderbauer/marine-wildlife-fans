import random

mwl_facts = [
    "Approximately 72% of the surface of the planet is covered by salt water. ",
    "It is believed that life in the ocean began approximately 3.1 to 3.4 billion years ago. It is believed that life on land began approximately 400 million years ago. This means that life in the ocean existed approximately 3 billion years before life on land. ",
    "Jellyfish have existed longer than dinosaurs and sharks; they have existed for more than 650 million years. A group of jellyfish are referred to as a smack. ",
    "An electric eel, which lives in the ocean, could power 10 light bulbs with its electricity. ",
    "When dolphins sleep only 50% of their brain actually sleeps and only one eye closes, so they can watch for predators. ",
    "Octopus' have blue blood and three hearts. ",
    "The blue whale's call is the loudest of any animal on earth, reaching 188 decibels. ",
    "The sea sponge is a living ocean animal yet it has no head, mouth, eyes, bones lungs, brain or even a heart. ",
    "The male seahorse, rather than the female, is the only animal known to man that gives birth and cares for its young. ",
    "Dolphins are able to hear sounds from up to 24 kilometers away under water. ",
    "The blue whale can grow as long as three Greyhound buses. It can weigh as much as 50 full grown elephants. The blood vessels of the blue whale are so large that a trout could swim through them. The heart of the blue whale is about the same size as a small car. ",
    "There are several species of deep sea animals living in the oceans that terrify humans including the dragonfish, frilled shark, vampire squid, big red jellyfish, giant squid, coffinfish, anglerfish, snaggletooth, and the blue ringed octopus. Some are poisonous while others have huge teeth and menacing appearances. ",
    "A small sample of ocean birds include the black-footed albatross, Atlantic puffin, several species of penguin, Eurasian oystercatcher, kingfisher, great cormorant, and different species of gulls. ",
    "A small sample of the different types of marine mammals include seals, whales, sea lions, dolphins, otters, porpoises, walruses, and manatees. ",
    "There are more than 230,000 known species living in the world's oceans. It is believed that only 5% of the world's oceans have been explored, which means there are likely hundreds of thousands or even millions of species of ocean animals that are undiscovered. "
]


def random_mwl_fact():
    return random.choice(list(mwl_facts))