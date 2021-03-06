#!/usr/bin/python
# -*- coding: utf-8 -*-

from joint import Joint
from chain import Chain
from chain import get_children

dummy_jnt_parameters = {
    'mu': 0,
    'sigma': 0,
    'gamma': 0,
    'b': 0,
    'alpha':0,
    'd':0,
    'theta': 0,
    'r': 0,
    }

jnt1 = Joint(antc=None, **dummy_jnt_parameters)
jnt2 = Joint(antc=jnt1, **dummy_jnt_parameters)
jnt3 = Joint(antc=jnt2, **dummy_jnt_parameters)
jnt4 = Joint(antc=jnt2, **dummy_jnt_parameters)
jnt5 = Joint(antc=jnt4, **dummy_jnt_parameters)
joints = [jnt1, jnt2, jnt3]
#print(jnt1)
#print(jnt2)
#print(jnt3)
#print(jnt4)
#print(jnt5)

chain = Chain(joints)
#print([chain.get_subchain_from(jnt) for jnt in get_children(joints, jnt1)])
assert(chain.base == jnt1)
assert(chain.tools == [jnt3])
assert(get_children(joints, jnt1) == [jnt2])
assert(get_children(joints, jnt2) == [jnt3])
assert(chain.get_subchain_from(jnt3) == [jnt3])
assert(chain.get_subchain_from(jnt2) == [jnt2, jnt3])
assert(chain.get_subchain_from(jnt1) == [jnt1, jnt2, jnt3])
assert(chain.get_subchain_to(jnt1) == [jnt1])
assert(chain.get_subchain_to(jnt2) == [jnt1, jnt2])
assert(chain.get_subchain_to(jnt3) == [jnt1, jnt2, jnt3])

joints = [jnt1, jnt2, jnt3, jnt4]
chain = Chain(joints)
assert(chain.base == jnt1)
assert(chain.tools == [jnt3, jnt4])
assert(get_children(joints, jnt1) == [jnt2])
assert(get_children(joints, jnt2) == [jnt3, jnt4])
assert(chain.get_subchain_from(jnt3) == [jnt3])
assert(chain.get_subchain_from(jnt4) == [jnt4])
assert(chain.get_subchain_from(jnt2) == [jnt2, [[jnt3], [jnt4]]])
assert(chain.get_subchain_from(jnt1) == [jnt1, jnt2, [[jnt3], [jnt4]]])
assert(chain.get_subchain_to(jnt3) == [jnt1, jnt2, jnt3])
assert(chain.get_subchain_to(jnt4) == [jnt1, jnt2, jnt4])

chain = Chain([jnt1, jnt2, jnt3, jnt4, jnt5])
assert(chain.tools == [jnt3, jnt5])
assert(chain.get_subchain_from(jnt4) == [jnt4, jnt5])
assert(chain.get_subchain_from(jnt1) == [jnt1, jnt2, [[jnt3], [jnt4, jnt5]]])
assert(chain.get_subchain_to(jnt3) == [jnt1, jnt2, jnt3])
assert(chain.get_subchain_to(jnt4) == [jnt1, jnt2, jnt4])
assert(chain.get_subchain_to(jnt5) == [jnt1, jnt2, jnt4, jnt5])

# Closed-loop mechanism
jnt1 = Joint(antc=None, **dummy_jnt_parameters)
jnt2 = Joint(antc=jnt1, **dummy_jnt_parameters)
jnt3 = Joint(antc=jnt1, **dummy_jnt_parameters)
jnt4 = Joint(antc=jnt2, **dummy_jnt_parameters)
jnt5 = Joint(antc=jnt3, sameas=jnt4, **dummy_jnt_parameters)
chain = Chain([jnt1, jnt2, jnt3, jnt4, jnt5])
assert(chain.get_subchain_to(jnt4) == [jnt1, jnt2, jnt4])
assert(chain.get_subchain_to(jnt5) == [jnt1, jnt3, jnt5])

