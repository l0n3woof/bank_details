# Bank Details API

## Intro

This api gives details about the banks.

## Endpoints

There are two endpoints both of which use post method :- 

1. 'ifsc/' In this endpoint we should provide IFSC code of a bank to get all the details of the bank
```json
{"ifsc":"BARB0DUMIYA"}
```

2. 'branch/' In this endpoint we have to provide two keys 'city' and 'bank name' which will provide us with all the branches of the given bank within the given city
```json
{{"bank":"ABHYUDAYA COOPERATIVE BANK LIMITED", "city": "MUMBAI"}}
```

## Installing and running

Install the dependencies of the api using the command :-

```bash
pip install -r requirements.txt
```
Then run the server :-

```bash
python manage.py runserver
```

## We assume you are using python3

