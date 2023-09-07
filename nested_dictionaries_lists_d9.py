#nesting Dictionary in a Dictionary

travel_log = {
    "France":{"cities_visited": ["Paris", "Lyon", "Marseille", "Nice", "Annecy", "Montpellier"], "total_visits": 20},
    "Portugal": {"cities_visited": ["Porto", "Lisbon", "Olhao", "Lagos", "Cascais", "Sintra"], "total visits": 2},
}

#nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lyon", "Marseille", "Nice", "Annecy", "Montpellier"],
        "total_visits": 20,
    },
    {
        "country":"Portugal",
        "cities_visited": ["Porto", "Lisbon", "Olhao", "Lagos", "Cascais", "Sintra"],
        "total_visits": 2,
    },
]