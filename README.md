For new services that we are going to write, we need to depend on a token registry as a dependency, to support single sign on. The services depend on the following behaviour of the token registry:

* Provides a token when `login` is called and the given credentials are valid. If not, an exception is raised.
* If there is already a valid token for a user when `login` is called, this token is re-used.
* The token is valid until `invalidate_token` is called, with immediate effect.
* By calling `is_valid_token` services get to know if a token is valid

### Kata

* Part 1: Test-drive a fake implementation of a TokenRegistry (an implementation that satisfies the behaviour, does not do any I/O and is not production-ready).
* Part 2: Write a more realistic implementation against the same tests (you can use file storage or sqllite).