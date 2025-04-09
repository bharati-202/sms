def result(**kwargs):
    total = 0
    print(f"{'Subject':<10} {'Score':<5}")
    print("-" * 15)
    for subject, score in kwargs.items():
        print(f"{subject:<10} {score:<5}")
        total += score
    print("-" * 15)
    print(f"{'Total':<10} {total:<5}")




result(marathi=60,hindi=65,english=70,maths=75)
result(marathi=60,english=70,maths=75)