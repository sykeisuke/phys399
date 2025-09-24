scores = {
    "Rio": {"Math": 85, "Science": 90, "English": 88},
    "Kaito": {"Math": 70, "Science": 75, "English": 82},
    "Reika": {"Math": 92, "Science": 88, "English": 95}
}

def calc_ave(subject_scores):
    total = 0
    for score in subject_scores.values():
        total += score
    return total / 3 

for name, subjects in scores.items():
    avg = calc_ave(subjects)
    print(name, "average:", avg)
