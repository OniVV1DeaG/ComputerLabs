import pytest
import simpy

import task1_python
from Lab004.numgen import GeoGenerator
from Lab004.generator import Generator, TrigonomicOperations
from Lab5.task1_2_simpy import System, customer_generator
import Lab5.task2_python

T1_REJECT = 0.32
T1_ACCEPT = 0.68
T1_LCMO = 1.92
T1_TCMO = 2.40

T2_REJECT = 0.05 #10e-4
T2_ACCEPT = 0.95#1
T2_L = 0.6383#10e-4

T2_REJECTN = 0
T2_ACCEPTN = 1
T2_LN = 1.5283#10e-4

def prepare_task1():
    lambda_value = 0.8
    limit = 1
    service_time = 1.2
    max_time = 2000
    oper = TrigonomicOperations(0.1)
    generator = Generator(oper)
    gg = GeoGenerator()
    server = task1_python.LimitedSingleServer(limit, generator, service_time, lambda_value)
    return server

def prepare_task1_simpy():
    env = simpy.Environment()
    system_capacity = 1
    arrival_rate = 0.5
    gg = GeoGenerator()

    oper = TrigonomicOperations(0.1)
    generator = Generator(oper)
    system = System(env, system_capacity, generator, 1, service_time= 1.2)
    return system, env, generator, arrival_rate

def test_theoretical_task1():
    server = prepare_task1()
    p_reject, p_accept, lcmo, tcmo = server.get_theoretical()
    assert round(p_reject, 2) == T1_REJECT
    assert round(p_accept, 2) == T1_ACCEPT
    assert round(lcmo, 2) == T1_LCMO
    assert round(tcmo, 2) == T1_TCMO

def test_experimental_task1():
    server = prepare_task1()
    server.simulate_system(2000)
    p_reject, p_accept = server.get_values()
    assert round(p_reject, 2) == pytest.approx(T1_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T1_ACCEPT, 1)

def test_experimental_task1_simpy():
    system, env, generator, arrival_rate = prepare_task1_simpy()
    env.process(customer_generator(env, system, generator, arrival_rate))
    env.run(until=2000)

    p_reject, p_accept, avg = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T1_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T1_ACCEPT, 1)

def prepare_task2_limit():
    num_servers = 4
    max_queue_length = 4
    arrival_time = 1
    service_time = 3

    system = Lab5.task2_python.System(num_servers, max_queue_length, arrival_time, service_time, True)
    return system

def prepare_task2_non_limit():
    num_servers = 4
    max_queue_length = 3
    total_time = 2000
    arrival_time = 1
    service_time = 3

    system = Lab5.task2_python.System(num_servers, None, arrival_time, service_time, True)
    return system

def test_theoretical_task2_limit():
    system = prepare_task2_limit()
    p_reject, p_accept, lq = system.get_theoretical()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 1)

def test_theoretical_task2_non_limit():
    system = prepare_task2_non_limit()
    p_reject, p_accept, lq = system.get_theoretical()
    assert round(p_reject, 2) == pytest.approx(T2_REJECTN, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPTN, 1)
    assert round(lq, 2) == pytest.approx(T2_LN, 1)

def test_experimental_task2_limit():
    system = prepare_task2_limit()
    total_time = 2000
    system.simulate(total_time)
    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 100)

def test_experimental_task2_non_limit():
    system = prepare_task2_non_limit()
    total_time = 2000
    system.simulate(total_time)
    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECTN, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPTN, 1)
    assert round(lq, 2) == pytest.approx(T2_LN, 100)

def prepare_task2_simpy():
    env = simpy.Environment()
    system_capacity = 5
    arrival_rate = 1
    gg = GeoGenerator()

    oper = TrigonomicOperations(0.1)
    generator = Generator(oper)
    system = System(env, system_capacity, generator, 4, service_time=3)
    return system, env, generator, arrival_rate

def test_experimental_task2_simpy():
    system, env, generator, arrival_rate = prepare_task2_simpy()
    env.process(customer_generator(env, system, generator, arrival_rate))
    env.run(until=2000)

    p_reject, p_accept, lq = system.get_values()
    assert round(p_reject, 2) == pytest.approx(T2_REJECT, 1)
    assert round(p_accept, 2) == pytest.approx(T2_ACCEPT, 1)
    assert round(lq, 2) == pytest.approx(T2_L, 1000)