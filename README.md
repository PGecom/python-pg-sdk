# PG Rewards SDK - Python

So you are a developer and will start accepting payments with moncash. The PG Rewards Payments SDK is the easiest way to complete the integration in record time. With the PG Rewards Payment SDK, you can create a payment process through moncash to meet the unique needs of your projects.

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
payment['redirectUrl'] #the redirect moncash link
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
client.Payment.get_payment_details("<orderId>")
```

For details of all the request and response parameters , check our [PG API Documentation guide](https://docs.pgecom.com/api-endpoint/mon-cash/retrieve-an-order-id)
On successful payment, the status in the response will change to **COMPLETED**
In case of a pending for Payment, the status in the response will change to **PENDING**

<hr>

### Task | workflow

- [x] Moncash
- [x] Payment details
- [ ] Card

<hr>
