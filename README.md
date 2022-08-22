Suppose that for new services that we are going to write, we depend on an authentication service, to support single sign on. The services depend on the following behaviour of the authentication service:

* Can register a new user with a password. User names must be unique.
* Provides a token when `login` is called and the given credentials are valid. If credentials are not valid, an exception is raised.
* If there is already a valid token for a user when `login` is called, this token is re-used.
* The token is valid until `invalidate_token` is called, with immediate effect.
* By calling `is_valid_token` services get to know if a token is valid

### Kata

* Part 1: Test-drive a fake implementation of `AuthenticationService` that we can use as test double (an implementation that satisfies the behaviour, but does not do any I/O).
* Part 2: Write a (more) realistic implementation against the same tests (you can use file storage, sqllite, ...). Do you need additional tests?
