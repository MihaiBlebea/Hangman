import csv

class Writer:

    folder = "database"

    def path(self, file):
        return "{}/{}".format(self.folder, file)

    def write_csv(self, file, payload):
        path = self.path(file)
        with open(path, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(payload)

    def write_txt(self, file, payload):
        path = self.path(file)
        txt_file = open(path, "w")
        txt_file.write(payload)
        txt_file.close()

    def read_txt(self, file):
        path = self.path(file)
        with open(path, "r") as txt_file:
            content = txt_file.read()
            txt_file.close()
            return content

    # Helper methods
    def hide_letters(self, word):
        letters = list(word)

        result = []
        for index, letter in enumerate(letters):
            if index == 0:
                result.append(letter)
            elif index == len(letters) - 1:
                result.append(letter)
            else:
                result.append("_")

        return "".join(result)
