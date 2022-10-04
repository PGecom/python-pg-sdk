![PG Rewards - API helps you create your virtual or physical and start spending online](https://uploads-ssl.webflow.com/632a265ac6a9500ac9e49d72/632bae11d162d0b07979e791_Pg%20Rewards%20Logo-01.png)

<div align="center">
  <h1>PG Rewards SDK - Python</h1>
</div>

<div align="center">
  <strong>The PG Rewards API SDK Python helps you create your virtual or physical and start spending online</strong>
</div>

<br>

<div align="center">
  Have a question or need some help?: <br>
  <a href="https://pgecom.com">Website</a>
  <span> | </span>
  <a href="mailto:info@pgecom.com">Email</a>
  <span> | </span>
  <a href="http://help.pgecom.com">Help</a>
</div>

<div align="center">
  So you are a developer and will start accepting payments with moncash. The PG Rewards Payments SDK is the easiest way to complete the integration in record time. With the PG Rewards Payment SDK, you can create a payment process through moncash to meet the unique needs of your projects.
</div>

## Table of Contents

- [Python Django Example](#python-django-example)
- [Getting an API Key](#getting-an-api-key)
- [Payment with Moncash](#create-a-paymet-with-mon-cash)
- [Payment Detail](#get-payment-details)
- [Send Rewards](#send-rewards)
- [Create Card](#card-schema)
- [Card Detail](#fetch-a-particular-card-details)
- [List Cards](#fetch-all-cards)

# Python Django Example
```sh
$ cd example
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```
## Getting an API Key

![](https://3711139374-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MNoNIWRBSpPI3RWl7Qz-1703796690%2Fuploads%2FJtcX4LUHzKUrW3CcgJtI%2FDeveloper%20Credentials.png?alt=media&token=3bb83868-6cd5-40f5-9be3-129f08f93cb7)
before we start the integration make sure you have:

- [Registered](https://devtopup.pgecom.com) for a PG Rewards developer Account
- Navigate to Settings > Developer Setting
- Click on Generate New Credentials to get new credentials

### Install pip package

```sh
$ pip install pgrwpy
```

## Getting Started

You need to setup your key and secret using the following:

To work in production mode you need to specify your production PG_USER_ID & PG_SECRET_KEY along with a production_mode True boolean flag

```py
import pgrwpy

client = pgrwpy.Client(auth=(PG_USER_ID, PG_SECRET_KEY),
                         production_mode=True)
```

or

To work in sandbox mode you need to specify your sandbox PG_USER_ID & PG_SECRET_KEY keys along with a False boolean flag or you could just omit the production_mode flag since it defaults to False if not specified

```py
import pgrwpy

client = pgrwpy.Client(auth=(PG_USER_ID, PG_SECRET_KEY),
                         production_mode=False)
```

After setting up the client instance you can get the current pgrwpy SDK version using the following:

```py
print(client.get_version())
```

### Create a paymet with Mon Cash

In order to receive payments using this flow, first of all you will need to create a Moncash payment. Following are the important parameters that you can provide for this method:

| Field       | Required | Type   | Description                                                           |
| ----------- | -------- | ------ | --------------------------------------------------------------------- |
| amount      | Yes      | number | Amount in Haitian Currency (gourdes)                                  |
| referenceId | Yes      | string | Your internal reference ID into your own system for tracking purposes |
| successUrl  | Yes      | string | Send the user back once the transaction is successfully complete      |
| errorUrl    | Yes      | string | Send the user back if there is an error with the transaction          |

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/mon-cash/mon-cash-schema)

```py
data = {
    "amount": 500,
    "referenceId": "12345test",
    "successUrl": "https://example.com",
    "errorUrl": "https://example.com"
}

payment = client.Payment.moncash(data)
print(payment['redirectUrl']) #the redirect moncash link
```

Did you get a **HTTP 201** response, if yes then you are all set for the next step.

<hr>

### Get Payment Details

Now that you have created a payment, the next step is to implement polling to get Payment Details. We recommend a 4-5 second interval between requests. Following are the important parameters that you can provide for this method:

| Field   | Required | Type   | Description                                                           |
| ------- | -------- | ------ | --------------------------------------------------------------------- |
| orderId | Yes      | string | Your internal reference ID into your own system for tracking purposes |

### Fetch a particular Moncash payment details

```py
res = client.Payment.get_payment_details("<orderId>")
print(res) # 200: OK
```

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/mon-cash/retrieve-an-order-id)
On successful payment, the status in the response will change to **COMPLETED**
In case of a pending for Payment, the status in the response will change to **PENDING**

<hr>

### Rewards Schema

You can use send rewards as a way to recharge a user's account. The funds will automatically be available on their virtual or physical card. Following are the important parameters that you can provide for this method:

| Field   | Required | Type    | Description                                  |
| ------- | -------- | ------- | -------------------------------------------- |
| email   | Yes      | string  | Recipient email                              |
| amount  | Yes      | number  | Amount for the recipient                     |
| prepaid | Yes      | boolean | User created via your platform, default true |

### Send rewards

```py
data = {
    "email": "info@pgecom.com",
    "amount": 10,
    "prepaid": False,
}
res = client.Reward.send(data)
print(res) # 200: OK
```

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/send-rewards/send-rewards)
Did you get a **HTTP 201** response, if yes then you are all set for the next step.

<hr>

### Card Schema

In order to create a card, you will need to send a request to us with the following parameters:

| Field          | Required | Type    | Description                                                                                                                                    |
| -------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| fullName       | Yes      | number  | Recipient that needs to be on the card                                                                                                         |
| amount         | Yes      | string  | Available mount to spend with the card                                                                                                         |
| email          | Yes      | string  | Email of the card recipient                                                                                                                    |
| billingAddress | Yes      | object  | Recipient address on the card. The country is required inside billingAddress                                                                   |
| physical       | Yes      | boolean | If set to true, then card shipped to the provided address - only shipping for physical USA                                                     |
| person         | Yes      | string  | prepaid/user - user is a registered user on the platform, and prepaid is just temporary prepaid card with a limited amount and limited feature |

The billing address object reference above

| Field       | Required | Type   | Description              |
| ----------- | -------- | ------ | ------------------------ |
| line1       | Yes      | string | recipient street address |
| city        | Yes      | string | recipient city           |
| country     | Yes      | string | recipient country        |
| state       | Yes      | string | recipient state          |
| postal_code | Yes      | number | recipient postal code    |

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/card/card-schema)

```py
data = {
    "fullName": "Stanley Castin",
    "amount": 5,
    "email": "stanley@ninja.root",
    "billingAddress": {
        "line1": "9700 Medlock Bridge Road",
        "city": "John Creeks",
        "country": "US",
        "state": "WA",
        "postal_code": "90098"
    },
    "physical": False,
    "person": "prepaid" # prepaid | user
}

res = client.Card.create(data)
print(res) # 200: OK
```

Did you get a **HTTP 201** response, if yes then you are all set for the next step.

<hr>

### Retrieve a single card

Now that you have created a card, the next step is to implement polling to get Card Details. We recommend a 4-5 second interval between requests. Following are the important parameters that you can provide for this method:

| Field        | Required | Type   | Description           |
| ------------ | -------- | ------ | --------------------- |
| cardId       | Yes      | string | the actual card id    |
| cardHolderId | Yes      | string | The owner of the card |

### Fetch a particular Card details

```py
res = client.Card.get_card_details("<cardId>", "<cardHolderId>")
print(res) # 200: OK
```

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/card/retrieve-a-single-card)

<hr>

### List cards

the next step is to implement polling to get all Cards. We recommend a 4-5 second interval between requests. Following are the important parameters that you can provide for this method:

| Field        | Required | Type   | Description           |
| ------------ | -------- | ------ | --------------------- |
| cardHolderId | Yes      | string | The owner of the card |

### Fetch all Cards

```py
res = client.Card.get_all_cards("<cardHolderId>")
print(res) # 200: OK
```

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/card/list-cards)

<hr>

### Task | workflow

- [x] Payment with Moncash
- [x] Payment Detail
- [x] Send Rewards
- [x] Create Card
- [x] Card Detail
- [x] List Cards

<hr>
