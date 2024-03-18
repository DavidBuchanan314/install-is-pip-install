# install-is-pip-install

[infomercial voice] Has this ever happened to you?

```
$ python3 -m install sampleproject
/usr/bin/python3: No module named install
```

The solution is here! Simply run `python3 -m pip install install-is-pip-install`, today!

From then onwards, `python3 -m install ...` should act exactly the same as `python3 -m pip install ...`.

Allow me to demonstrate:

```yaml
$ python3 -m pip install install-is-pip-install
...
Installing collected packages: install-is-pip-install
Successfully installed install-is-pip-install-1.0
$ python3 -m install sampleproject
NOTICE: You just used install-is-pip-install!
...
Installing collected packages: peppercorn, sampleproject
Successfully installed peppercorn-0.6 sampleproject-3.0.0
```

Wow! This unprecedented functionality is all thanks to our [Secret Formula](https://github.com/DavidBuchanan314/install-is-pip-install/blob/main/src/install.py). Once again, that's `python3 -m pip install install-is-pip-install`. Install today!
