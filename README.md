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
$ python3.9 -m venv venv
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
Python 3.9.0 (default, Oct 25 2020, 08:40:04)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from example.rodi_test import rodi_main

In [2]: from example.punq_test import punq_main

In [3]: %timeit rodi_main()
9.06 µs ± 14.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [4]: %timeit rodi_main()
9.25 µs ± 106 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [5]: %timeit punq_main()
261 µs ± 899 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [6]: %timeit punq_main()
254 µs ± 331 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
