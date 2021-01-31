# Performance comparison between rodi and punq

[`rodi`](https://github.com/Neoteroi/rodi) and [`punq`](https://github.com/bobthemighty/punq) are both unobstrusive libraries to implement dependency
injection for Python 3.
This repository contains the same example from `punq` README file implemented
with both libraries, under the `example` module.

In this example, `rodi` is **~25 | ~27 times** faster than `punq` in resolving
services. This difference is explained by an implementation detail:
* `punq` runs type inspections each time a service needs to be resolved /
  activated
* `rodi` instead runs type inspections only once, and creates factory functions
  in memory to activate services

## How to run the tests with ipython

Create a Python virtual environment, then install requirements

```
$ python -m venv venv
```

Activate the virtual environment:

```
# Linux, Mac
$ source venv/bin/activate

# Windows
$ venv\Scripts\activate
```

Install requirements

```
$ pip install -r requirements.txt
```

Run `ipython`:

```
$ ipython
```

Import the functions and use `%timeit` to measure functions' performance:

```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from example.rodi_test import rodi_main

In [2]: from example.punq_test import punq_main

In [3]: %timeit rodi_main()
6.6 µs ± 394 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [4]: %timeit rodi_main()
6.39 µs ± 320 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [5]: %timeit punq_main()
176 µs ± 7.4 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [6]: %timeit punq_main()
181 µs ± 14.3 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```
