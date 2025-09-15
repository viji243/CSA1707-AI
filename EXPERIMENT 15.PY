# tiny_id3.py
from collections import Counter, defaultdict
import math

def entropy(rows):
    labels = [r[-1] for r in rows]
    total = len(labels)
    return -sum((count/total)*math.log2(count/total) for count in Counter(labels).values())

def split(rows, col):
    groups = defaultdict(list)
    for r in rows:
        groups[r[col]].append(r)
    return groups

def info_gain(rows, col):
    base = entropy(rows)
    groups = split(rows, col)
    total = len(rows)
    remainder = sum((len(g)/total)*entropy(g) for g in groups.values())
    return base - remainder

def build_tree(rows, feature_names):
    labels = [r[-1] for r in rows]
    if len(set(labels)) == 1:
        return ("leaf", labels[0])
    if not feature_names:
        return ("leaf", Counter(labels).most_common(1)[0][0])
    gains = [(info_gain(rows, i), i) for i in range(len(feature_names))]
    best_gain, best_col = max(gains)
    if best_gain == 0:
        return ("leaf", Counter(labels).most_common(1)[0][0])
    tree = ("node", feature_names[best_col], {})
    groups = split(rows, best_col)
    new_feats = feature_names[:best_col] + feature_names[best_col+1:]
    for val, subset in groups.items():
        subtree = build_tree([r[:best_col]+r[best_col+1:] for r in subset], new_feats)
        tree[2][val] = subtree
    return tree

def classify(tree, sample, feature_names):
    node_type = tree[0]
    if node_type == "leaf": return tree[1]
    _, feat, branches = tree
    val = sample[feature_names.index(feat)]
    branch = branches.get(val)
    if branch is None:
        return None
    # if branch is node, continue; if leaf return
    if branch[0] == "leaf": return branch[1]
    # rebuild feature list for recursive call
    new_features = [f for f in feature_names if f != feat]
    return classify(branch, [v for i,v in enumerate(sample) if feature_names[i] != feat], new_features)

# Example tiny dataset: weather/play
if __name__ == "__main__":
    # features: Outlook, Temperature, Humidity, Wind; label: Play?
    data = [
        ["Sunny","Hot","High","Weak","No"],
        ["Sunny","Hot","High","Strong","No"],
        ["Overcast","Hot","High","Weak","Yes"],
        ["Rain","Mild","High","Weak","Yes"],
        ["Rain","Cool","Normal","Weak","Yes"],
        ["Rain","Cool","Normal","Strong","No"],
        ["Overcast","Cool","Normal","Strong","Yes"],
    ]
    feats = ["Outlook","Temperature","Humidity","Wind"]
    tree = build_tree(data, feats)
    print("Tree:", tree)
    sample = ["Sunny","Cool","High","Strong"]
    print("Classify", sample, "->", classify(tree, sample, feats))
