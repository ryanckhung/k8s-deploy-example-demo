# generate a private key

> openssl genrsa -out testkey.key 2048

# sign a cert base on the private key

> openssl req -new -x509 -key testkey.key -out testkey.cert -days 3650
> (answer the questions for signing a cert.)

# take a look on the generated cert

> openssl x509 -in testkey.cert -text

Remark: private key and cert is not necessary for making a secret
secret can be anything you like, this just show an example to put the key and cert into the secret

# create some files for adding into the secret

> echo ryanckhung > username
> echo password > password

# crate a secret

> kubectl create secret generic ryan-secret --from-file=testkey.key --from-file=testkey.cert --from-file=username --from-file=password

# check the created k8s secret

> kubectl describe secret/ryan-secret
> kubectl get secret/ryan-secret -o yaml

all the 4 values are encoded into base64

> echo <content> | base64 -d
