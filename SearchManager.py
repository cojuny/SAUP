from SemanticSearch import SemanticSearch


if __name__ == '__main__':
    query = "She quickly finished her work and left the office."
    target_sentences = [
        "She quickly finished her work and left the office.",
        "She wrapped up her work promptly and walked out of the office.",
        "The sun set slowly behind the mountains, casting a warm glow over the landscape."
    ]
    
    engine = SemanticSearch()
    engine.search(query, target_sentences)
    
