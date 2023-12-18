python -m venv myenv


myenv\Scripts\activate


need python 3.8


to know your YouTube Data API v3  is work try this in google chrome   

https://www.googleapis.com/youtube/v3/search?part=id&channelId=UCfiwzLy-8yKzIbsmZTzxDgw&type=video&eventType=live&key=YOUR API HERE


THEN YOU WILL SEE RESPOND LIKE THIS :     


{
  "kind": "youtube#searchListResponse",
  "etag": "1D8ET5cPDKU2ascq5JEhjKfD-UA",
  "regionCode": "PS",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "T0y_Qu52v00QgYMmlYgzkPKjwtg",
      "id": {
        "kind": "youtube#video",
        "videoId": "bNyUyrR0PHo"
      }
    }
  ]
}
