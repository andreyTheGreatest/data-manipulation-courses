import sys
import json


def make_dict_of_scores(afinn_file):
    scores = {}  # initialize an empty dictionary
    for line in afinn_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    afinn_file.seek(0)
    return scores


def process_tweet(tweet_file, scores):
    for line in tweet_file:
        current_score = 0
        json_data = json.loads(line)
        text = json_data['text'] if 'text' in json_data else ""
        words = text.split()
        for word in words:
            current_score += scores[word] if word in scores else 0
        print current_score
    tweet_file.seek(0)


def main():
    afinn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = make_dict_of_scores(afinn_file)
    process_tweet(tweet_file, scores)


if __name__ == '__main__':
    main()
