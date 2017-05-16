from charms.reactive import when, when_not, set_state

import charmhelpers.fetch

_gitlab_source = "deb https://packages.gitlab.com/runner/gitlab-ci-multi-runner/ubuntu/ xenial main"
_gitlab_gpg_key = """
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.11 (GNU/Linux)

mQINBFUxDA4BEAC0Pwepk/QZK7QOv6loLtUqmPCJtUuOS3Gu410FoOCgh5agWmXe
J2pCTejLIMWPEG1Q35lrv5PRlcRA+XLIcYd6x7pF4+sDE1lOZVBndUMSHDReq+r+
lzRB0Rd6S75RshBRDuwHfBfzjmFcyPqqYdiY3YUqk+hHl/w8m5QlxgLDnp2Vjh2B
yzJqDtJh2+TmvY4XD91Q1fvihZkN3RFBgIjjs4xVQ+wptjg8FsPovgA+QED+hkFc
bBveClexICHi6mTFG+1HV1MfcZnIRDlggTCUj/U8TGnU5crs6GVbbxtKfTCAZYlQ
k5Q2JoPE4156wNFPQ7/Eyr3GnP62oySmuaCDzVVOlnmu4GMTVq/LVQZV3wOAdHM1
+9i0ob/SLYT5QKuL5jYj99rz2wy4HWxGR6TrSc/Ls0sc2MvZBeIXpOsPI2rxOeS+
3Kbz8E+0ezNWxHC2LBQezW1ikNfLow/vwIBDCS9ApDAdW8VN28cROoiCMd6yxnVI
1P2nMCkDMCBNqvcWtGrhUvpFD4jfaQ8661GEspqMbrXuNQ//JsrD9n98dJDWdCUV
0LWBEyAJTOV9kIEH128MlPK8SLNkvCBZNJS4pzUxJFmf3LbDmYMuqcgz1d5NltMk
tzVEpVJ4tgZ0gyn4f/yuZHobq6hP1YHgu3lNt7Aibi6dX5pfw2oWqufuPwARAQAB
tEJHaXRMYWIgQi5WLiAocGFja2FnZSByZXBvc2l0b3J5IHNpZ25pbmcga2V5KSA8
cGFja2FnZXNAZ2l0bGFiLmNvbT6JAj4EEwECACgFAlUxDA4CGwMFCQlmAYAGCwkI
BwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEBQhmpbhXnj0iN0QAIGHf0CShvrEZXOq
8Tlq+zJ42CQTOLa9Hijd85mqwijgoBwCdLaePaOqOBIkqev3UDfcoMJP9/JuXMpI
9H+JvfY/USwP7FVTpdyC+iecWOSJ/qdbxJEau2wyGwsVhcas9iOExzd6tjsS61Td
1bpdTBYG7eAenCu5WYU/cb0OhPbzRuUiLrtpt43tx2cXIU+XcEC/R9aym7EPw3WG
SePegNhKbtr3LaTuRswgO464LHgJ0YsUx9789QSyuhHtQGznBpBDj0F/xVjnxRs4
6vpd46AWad0G7RhDCWduuG0qx1/1ZBbQKKjRq/1Uw54qiVJB0T/7qtQ9OliUonDj
Vgkj3w1HGXTwKVSkDwEqyn+SDWERA9k04DQrOLEG0qi9NGLYy59v4SaU3ftZw0L6
jnCJksnACtrsksJWPI0Gbs+wbII6fhu8Zc1iV3hdzi92lDMv0W1KzM7FCrz3ex6i
3oL+ntZW/PuHNSUVBlr2FkkSr/EmRkBoD9efZsG7+5vYImtkSZSaiMi5IsexjTEH
HkP0xG0OUaCagSNrNolDyLEmTjhOmky67oE1VIOIbMajXzeNdqYahz8+kBQ5vgpr
0PqlNbnVgCiTlFjTVGHUj84SKh/Gii+GRHlCV1d5UL/GzJppZ5MfpjRXOTamqU/C
O0JLVZiTnW+KSqbLEdflanh8IPTF
=jmzU
-----END PGP PUBLIC KEY BLOCK-----
""".strip()

@when_not('gitlab-runner.installed')
def install_gitlab_runner():
    charmhelpers.fetch.add_source(_gitlab_source, _gitlab_gpg_key)
    charmhelpers.fetch.apt_update()
    charmehlpers.fetch.apt_install(["gitlab-ci-multi-runner"])
    set_state('gitlab-runner.installed')

#TODO(axw) gitlab-runner relation
#@when('gitlab-runner.installed')
