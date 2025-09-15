def compare_decision_tree_and_mlp():
    # small synthetic dataset (Iris-like)
    try:
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.neural_network import MLPClassifier
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=1)
        dt = DecisionTreeClassifier(max_depth=5).fit(X_train, y_train)
        mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000).fit(X_train, y_train)
        return {
            'decision_tree_score': dt.score(X_test, y_test),
            'mlp_score': mlp.score(X_test, y_test)
        }
    except Exception as e:
        return {'error': str(e)}
