import pytest
 
def resource_1_setup():
    print('Setup for resource 1 called')
 
def resource_1_teardown():
    print('Teardown for resource 1 called')
 
def setup_module(module):
    print('\nSetup of module is called')
    resource_1_setup()
 
def teardown_module(module):
    print('\nTeardown of module is called')
    resource_1_teardown()
 
def test_1_using_resource_1():
    print('Test 1 that uses Resource 1')
 
def test_2_not_using_resource_1():
    print('\nTest 2 does not need Resource 1')