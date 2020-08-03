import pytumblr

client = pytumblr.TumblrRestClient(

    '1NqX9WQBseVqnuWpOJyXGq7DTKtFpaXZWqNbOT0fCp7iXe6wm1',
    'iBfMARl2yxCb8eRps4V76BFWAGiikmOLwSkrE2ESfKuWx2ER6Q',
    'y0xFUJTdFqW88EnxGOoutZPusjA1q3wSRUPjLKJET2RbH2WOjX',
    'jdxDw0MM2jp4jNLKEZT0IEpnuhxwO5vVBdgO1B6EC1FnsQHS4Y'
)

print(client.info())

