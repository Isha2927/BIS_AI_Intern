import pandas as pd

def load_knowledge_base():

    df = pd.read_csv("knowledge_base/lab_tests.csv")

    knowledge = {}

    for _, row in df.iterrows():

        knowledge[row["test_name"]] = {
            "description": row["description"],
            "low_meaning": row["low_meaning"],
            "high_meaning": row["high_meaning"]
        }

    return knowledge