import csv
import pickle


class Serializer:

    @staticmethod
    def serialize_csv(path, dict_list):
        with open(path, "w", newline="") as file:
            columns = ['numeral', 'denominator']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for dictionary in dict_list:
                writer.writerow(dictionary.values())

    @staticmethod
    def deserialize_csv(path, dict_list: list):
        with open(path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dict_list.append(row)

    @staticmethod
    def serialize_pickle(path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def deserialize_pickle(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data