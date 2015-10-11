import json

def make_csv():
    file = open("transcript.txt","r")
    text = file.read()
    file.close()
    #get rid of double newlines
    #while "\n\n" in text:
    #    text = text.replace("\n\n", "\n")
    text = text.replace("\n", ' ')
    #remove all commas
    for undesirable in [',','.',';','?', '-']:
        while undesirable in text:
            text = text.replace(undesirable, " ")
    #replace colons with commas
    #text = text.replace(":",",")
    #replace all prompts
    for prompt in [
        "BUSH",
        "TAPPER",
        "PAUL",
        "HUCKABEE",
        "RUBIO",
        "TRUMP",
        "CRUZ",
        "CARSON",
        "WALKER",
        "FIORINA",
        "KASICH",
        "CHRISTIE"
    ]:
        text = text.replace(prompt + ':', '\n' + prompt + ',')
    file = open("better.csv", "w")
    file.write(text)
    file.close()

def make_json():
    file = open("better.csv", "r")
    out_records = []
    index = 0
    for line in file.readlines():
        (name, passage) = line.split(',')
        out_records.append({
            'name': name,
            'passage': passage,
            'index': index
        })
        index += 1
    file.close()
    file = open("debate.json", "w")
    file.write(json.dumps(out_records))
    file.close()

def make_json_whitelist():
    whitelist = ["Iraq", "Change", "Economy", "Business", "Change", "jobs", "reform", 'god', 'character', 'disgusting', 'obama', 'obamacare', 'healthcare', 'family', 'tax', 'taxes', 'liberal', 'conservative', 'war', 'syria','china', 'oil']
    whitelist = map(lambda x: x.upper().strip(), whitelist)
    file = open("better.csv", "r")
    out_records = []
    index = 0
    for line in file.readlines():
        (name, passage) = line.split(',')
        passage_words = passage.split(' ')
        for word in passage_words:
            word = word.upper().strip()
        passage = " ".join(passage_words)

        out_records.append({
            'name': name,
            'passage': passage,
            'index': index
        })
        index += 1
    file.close()
    file = open("debate-whitelist.json", "w")
    file.write(json.dumps(out_records))
    file.close()

if __name__ == '__main__':
    #make_csv()
    make_json()
