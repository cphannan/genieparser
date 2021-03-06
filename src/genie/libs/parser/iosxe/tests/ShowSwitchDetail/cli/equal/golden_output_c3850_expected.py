expected_output = {
    "switch": {
        "stack": {
            "1": {
                "role": "active",
                "hw_ver": "V04",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 3},
                    "2": {"stack_port_status": "ok", "neighbors_num": 2},
                },
                "state": "ready",
                "priority": "3",
                "mac_address": "689c.e2ff.b9d9",
            },
            "3": {
                "role": "member",
                "hw_ver": "V05",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 2},
                    "2": {"stack_port_status": "ok", "neighbors_num": 1},
                },
                "state": "ready",
                "priority": "1",
                "mac_address": "c800.84ff.4800",
            },
            "2": {
                "role": "standby",
                "hw_ver": "V05",
                "ports": {
                    "1": {"stack_port_status": "ok", "neighbors_num": 1},
                    "2": {"stack_port_status": "ok", "neighbors_num": 3},
                },
                "state": "ready",
                "priority": "2",
                "mac_address": "c800.84ff.7e00",
            },
        },
        "mac_address": "689c.e2ff.b9d9",
        "mac_persistency_wait_time": "indefinite",
    }
}
