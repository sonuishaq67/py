import requests

def create_query(languages,min_stars=5000): 
    query=f"stars:>{min_stars} "
    for language in languages:
        query+=f"language:{language} "
    return query

def repo_with_stars(languages,sort="stars",order="desc"):
    api_url = "http://api.github.com/search/repositories"
    parameters={"q":f"{create_query(languages)}","sort":sort,"order":order}
    response = requests.get(api_url,params=parameters)
    print("status code is ", response.status_code)
    return response.json()["items"]


if __name__=="__main__":
    languages=["Python","Javascript","C"]
    results=repo_with_stars(languages)
    for result in results:
        language=result["language"]
        stars=result["stargazers_count"]
        name=result["name"]
        print("language is ",language," stars are ",stars," name is ",name)