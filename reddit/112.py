import praw
import hidden
import matplotlib.pyplot as plt

common_english_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her",
    "she", "or", "an", "will", "my", "one", "all", "would", "there",
    "their", "what", "so", "up", "out", "if", "about", "who", "get",
    "which", "go", "me", "when", "make", "can", "like", "time", "no",
    "just", "him", "know", "take", "people", "into", "year", "your",
    "good", "some", "could", "them", "see", "other", "than", "then",
    "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first",
    "well", "way", "even", "new", "want", "because", "any", "these",
    "give", "day", "most", "us", "is", "are", "was", "were", "been",
    "have", "had", "has", "do", "does", "did", "am", "isn't", "aren't",
    "wasn't", "weren't", "hasn't", "haven't", "hadn't", "doesn't",
    "don't", "didn't", "won't", "wouldn't", "shan't", "shouldn't",
    "can't", "cannot", "couldn't", "mustn't", "let's", "that's",
    "who's", "what's", "here's", "there's", "where's", "when's",
    "why's", "which's", "whose", "whom's", "whichever", "whomever",
    "whatever", "whensoever", "whencesoever", "wheresoever", "whichsoever",
    "whysoever", "he's", "she's", "it's", "I'm", "you're", "we're",
    "they're", "he'll", "she'll", "it'll", "I'll", "you'll", "we'll",
    "they'll", "he'd", "she'd", "it'd", "I'd", "you'd", "we'd",
    "they'd", "here", "there", "where", "when", "why", "which",
    "what", "who", "whom", "whose", "whichever", "whomever",
    "whatever", "whensoever", "whencesoever", "wheresoever",
    "whichsoever", "whysoever", "up", "down", "in", "out", "off",
    "on", "over", "under", "above", "below", "between", "among",
    "through", "around", "before", "after", "near", "far", "away",
    "with", "without", "within", "into", "onto", "upward", "downward",
    "backward", "forward", "inside", "outside", "here", "there", "where",
    "when", "why", "which", "what", "who", "whom", "whose", "how",
    "somewhere", "anywhere", "nowhere", "everywhere", "elsewhere",
    "now", "then", "today", "yesterday", "tomorrow", "soon", "later",
    "early", "nowadays", "immediately", "recently", "already", "soon",
    "later", "before", "after", "then", "now", "today", "yesterday",
    "tomorrow", "again", "never", "always", "sometimes", "often",
    "seldom", "rarely", "usually", "occasionally", "frequently",
    "constantly", "continuously", "regularly", "daily", "weekly",
    "monthly", "yearly", "annually", "hourly", "suddenly", "quickly",
    "slowly", "easily", "hardly", "barely", "scarcely", "mostly",
    "mostly", "partly", "completely", "almost", "absolutely", "rather",
    "somewhat", "much", "many", "little", "few", "more", "less",
    "most", "least", "several", "some", "any", "no", "none", "all",
    "each", "every", "both", "either", "neither", "none", "other",
    "another", "such", "the", "this", "that", "these", "those",
    "a", "an", "my", "your", "his", "her", "its", "our", "their"
]

reddit = praw.Reddit(
    client_id=hidden.client_id,
    client_secret=hidden.client_secret,
    user_agent="112",
)
words = {}


subredditname = "memes"
for post in reddit.subreddit(subredditname).hot(limit=1):
    post.comments.replace_more(limit=0)
    for comment in post.comments:
        body = comment.body.strip().lower()
        split = body.split(" ")
        for i in split:
            if i in common_english_words: continue
            if i not in words:
                words[i] = 0
            words[i] += 1

bruh = sorted(words.items(), key=lambda item: item[1], reverse=True)
sizes = []
labels = []
for i in range(10):
    sizes.append(bruh[i][1])
    labels.append(bruh[i][0])

plt.title('Top comments for: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

plt.savefig("pedemees.png")