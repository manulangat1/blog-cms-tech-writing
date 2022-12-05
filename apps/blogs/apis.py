import requests


class MediumAPI:
    def __init__(self, token):
        self.token = token

    def get_userId(token):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Host": "api.medium.com",
            "TE": "Trailers",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        }
        url = "https://api.medium.com/v1"
        response = requests.get(
            url=url + "/me",  # https://api.medium.com/me
            headers=header,
            params={"accessToken": token},
        )
        my_id = ""
        # checking response from server
        if response.status_code == 200:
            response_json = response.json()
            userId = response_json["data"]["id"]
            my_id = userId
        return my_id

    def post_to_medium(id, token, post):
        # id = self.get_userId(token)
        posturl = f"https://api.medium.com/v1/users/{id}/posts"
        postHeader = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Host": "api.medium.com",
            "TE": "Trailers",
            "Authorization": f"Bearer {token}",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        }

        tags = [i.title for i in post.tags.all()]
        data = {
            "title": post.title,
            "contentFormat": "markdown",
            "content": post.content,
            "tags": [],
            "canonicalUrl": "https://blog.kipchirchirlangat.com/" + "post.slug",
            # "public" will publish to gibubfor putting draft use value "draft"
            "publishStatus": "draft",
        }
        postRes = requests.post(posturl, headers=postHeader, data=data)
        return postRes


z = "88c58138-2bd9-449a-9383-3b697eddfe16"


class HashnodeAPI:
    def __init__(self, token):
        self.token = token

    def get_articles(z):
        headers = {"Authorization": f"{z}"}
        query = """
        query {
            user(username: "manulangat") {
                username
                name
                tagline
                numFollowers
                publicationDomain
                publication{
                posts{
                    slug
                        title
                        brief
                        coverImage
                    contentMarkdown

                }
                }
            }
            }
        """
        response = requests.post(
            url="https://api.hashnode.com", json={"query": query}, headers=headers
        )
        if response.status_code == 200:
            posts = response.json()["data"]["user"]["publication"]["posts"]
            return posts
        else:
            raise Exception(
                "Query failed to run by returning code of {}.".format(response.text)
            )
