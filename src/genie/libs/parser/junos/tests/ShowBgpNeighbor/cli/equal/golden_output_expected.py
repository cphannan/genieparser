expected_output = {
    "bgp-information": {
        "bgp-peer": [
            {
                "bgp-option-information": {
                    "bgp-options": "Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "v4_pyats_NO-DEFAULT",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "720",
                    "import-policy": "11",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "v4_pyats",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.49.216.179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_pyats",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-bfd": {
                    "bfd-configuration-state": "disabled",
                    "bfd-operational-state": "down",
                },
                "bgp-error": [
                    {
                        "name": "Hold Timer Expired Error",
                        "receive-count": "17",
                        "send-count": "156",
                    },
                    {"name": "Cease", "receive-count": "6", "send-count": "0"},
                ],
                "bgp-option-information": {
                    "address-families": "inet-unicast inet-labeled-unicast",
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown AddressFamily PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "bgp-output-queue": [
                    {
                        "count": "0",
                        "number": "1",
                        "rib-adv-nlri": "inet-unicast",
                        "table-name": "inet.0",
                    },
                    {
                        "count": "0",
                        "number": "2",
                        "rib-adv-nlri": "inet-labeled-unicast",
                        "table-name": "inet.3",
                    },
                ],
                "bgp-peer-iosession": {
                    "iosession-state": "Enabled",
                    "iosession-thread-name": "bgpio-0",
                },
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "684",
                        "active-prefix-count": "682",
                        "advertised-prefix-count": "0",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet.0",
                        "received-prefix-count": "684",
                        "rib-bit": "20000",
                        "send-state": "in sync",
                        "suppressed-prefix-count": "0",
                    },
                    {
                        "accepted-prefix-count": "2",
                        "active-prefix-count": "2",
                        "advertised-prefix-count": "0",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet.3",
                        "received-prefix-count": "2",
                        "rib-bit": "30000",
                        "send-state": "in sync",
                        "suppressed-prefix-count": "0",
                    },
                ],
                "active-holdtime": "30",
                "peer-id": "10.169.14.240",
                "local-id": "10.189.5.252",
                "description": "sjkGDS221-EC11",
                "entropy-label": "No",
                "entropy-label-capability": "Yes",
                "entropy-label-no-next-hop-validation": "Yes",
                "entropy-label-stitching-capability": "Yes",
                "flap-count": "127",
                "group-index": "10",
                "input-messages": "280022",
                "input-octets": "7137084",
                "input-refreshes": "0",
                "input-updates": "61419",
                "keepalive-interval": "10",
                "last-checked": "1999164",
                "last-error": "Hold Timer Expired Error",
                "last-event": "RecvKeepAlive",
                "last-flap-event": "HoldTime",
                "last-received": "3",
                "last-sent": "3",
                "last-state": "OpenConfirm",
                "local-address": "10.189.5.252+179",
                "local-as": "65171",
                "local-ext-nh-color-nlri": "inet-unicast",
                "nlri-type": "inet-labeled-unicast",
                "nlri-type-peer": "inet-unicast inet-labeled-unicast",
                "nlri-type-session": "inet-unicast inet-labeled-unicast",
                "output-messages": "221176",
                "output-octets": "4202359",
                "output-refreshes": "0",
                "output-updates": "0",
                "peer-4byte-as-capability-advertised": "65151",
                "peer-addpath-not-supported": True,
                "peer-address": "10.169.14.240+60606",
                "peer-as": "65151",
                "peer-cfg-rti": "master",
                "peer-end-of-rib-received": "inet-unicast inet-labeled-unicast",
                "peer-end-of-rib-sent": "inet-unicast inet-labeled-unicast",
                "peer-flags": "Sync",
                "peer-fwd-rti": "master",
                "peer-group": "sjkGDS221-EC11",
                "peer-index": "0",
                "peer-no-llgr-restarter": True,
                "peer-no-restart": True,
                "peer-refresh-capability": "2",
                "peer-restart-flags-received": "Notification",
                "peer-restart-nlri-configured": "inet-unicast inet-labeled-unicast",
                "peer-restart-nlri-negotiated": "inet-unicast inet-labeled-unicast",
                "peer-stale-route-time-configured": "300",
                "peer-state": "Established",
                "peer-type": "External",
                "snmp-index": "15",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "obpGCS001-WC11",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.169.14.249",
                "peer-as": "65151",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "obpGCS001-WC11",
                "peer-state": "Active",
                "peer-type": "External",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "ALL_out",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "import-policy": "REJ_LONG_ASPATH",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "cm-hkm003",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "ConnectRetry",
                "last-state": "Active",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.5.240+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_RRC_72_SQUARE",
                "peer-state": "Connect",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "ALL_out",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "import-policy": "REJ_LONG_ASPATH",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "cm-hkm004",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "ConnectRetry",
                "last-state": "Active",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.5.241+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_RRC_72_SQUARE",
                "peer-state": "Connect",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "cm-hkt003",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.5.242",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_RRC_72_TRIANGLE",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "cm-hkt004",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.5.243",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_RRC_72_TRIANGLE",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "lg-hkt001",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.5.245",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v4_RRC_72_TRIANGLE",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-bfd": {
                    "bfd-configuration-state": "disabled",
                    "bfd-operational-state": "down",
                },
                "bgp-error": [
                    {
                        "name": "Hold Timer Expired Error",
                        "receive-count": "36",
                        "send-count": "18",
                    },
                    {"name": "Cease", "receive-count": "2", "send-count": "10"},
                ],
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "bgp-output-queue": [
                    {
                        "count": "0",
                        "number": "1",
                        "rib-adv-nlri": "inet-unicast",
                        "table-name": "inet.0",
                    }
                ],
                "bgp-peer-iosession": {
                    "iosession-state": "Enabled",
                    "iosession-thread-name": "bgpio-0",
                },
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "682",
                        "active-prefix-count": "0",
                        "advertised-prefix-count": "682",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet.0",
                        "received-prefix-count": "682",
                        "rib-bit": "20001",
                        "send-state": "in sync",
                        "suppressed-prefix-count": "0",
                    }
                ],
                "description": "hktGCS002",
                "flap-count": "44",
                "group-index": "0",
                "input-messages": "110633",
                "input-octets": "2104771",
                "input-refreshes": "0",
                "input-updates": "4",
                "keepalive-interval": "20",
                "last-checked": "1999134",
                "last-error": "Hold Timer Expired Error",
                "last-event": "RecvKeepAlive",
                "last-flap-event": "RecvNotify",
                "last-received": "13",
                "last-sent": "3",
                "last-state": "OpenConfirm",
                "local-address": "10.189.5.252+60144",
                "local-as": "65171",
                "local-ext-nh-color-nlri": "inet-unicast",
                "nlri-type-peer": "inet-unicast",
                "nlri-type-session": "inet-unicast",
                "output-messages": "171942",
                "output-octets": "5078640",
                "output-refreshes": "0",
                "output-updates": "61307",
                "peer-4byte-as-capability-advertised": "65171",
                "peer-addpath-not-supported": True,
                "active-holdtime": "60",
                "peer-id": "10.189.5.253",
                "local-id": "10.189.5.252",
                "peer-address": "10.189.5.253+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-end-of-rib-received": "inet-unicast",
                "peer-end-of-rib-sent": "inet-unicast",
                "peer-flags": "Sync",
                "peer-fwd-rti": "master",
                "peer-group": "hktGCS002",
                "peer-index": "0",
                "peer-no-llgr-restarter": True,
                "peer-no-restart": True,
                "peer-refresh-capability": "2",
                "peer-restart-flags-received": "Notification",
                "peer-restart-nlri-configured": "inet-unicast",
                "peer-restart-nlri-negotiated": "inet-unicast",
                "peer-stale-route-time-configured": "300",
                "peer-state": "Established",
                "peer-type": "Internal",
                "snmp-index": "0",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "10.189.5.252",
                    "preference": "170",
                },
                "description": "sggjbb001",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "10.189.5.252",
                "local-as": "65171",
                "peer-address": "10.189.6.250",
                "peer-as": "65181",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "sggjbb001",
                "peer-state": "Active",
                "peer-type": "External",
            },
            {
                "bgp-option-information": {
                    "bgp-options": "Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "v6_Kentik_NO-DEFAULT",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "720",
                    "import-policy": "11",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "v6_Kentik",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "ConnectRetry",
                "last-state": "Active",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:6be:89bb::1:140+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_Kentik",
                "peer-state": "Connect",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-bfd": {
                    "bfd-configuration-state": "disabled",
                    "bfd-operational-state": "down",
                },
                "bgp-error": [
                    {
                        "name": "Hold Timer Expired Error",
                        "receive-count": "24",
                        "send-count": "171",
                    },
                    {"name": "Cease", "receive-count": "5", "send-count": "0"},
                ],
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "bgp-output-queue": [
                    {
                        "count": "0",
                        "number": "3",
                        "rib-adv-nlri": "inet6-unicast",
                        "table-name": "inet6.0",
                    }
                ],
                "bgp-peer-iosession": {
                    "iosession-state": "Enabled",
                    "iosession-thread-name": "bgpio-0",
                },
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "0",
                        "active-prefix-count": "0",
                        "advertised-prefix-count": "0",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet6.0",
                        "received-prefix-count": "0",
                        "rib-bit": "40000",
                        "send-state": "in sync",
                        "suppressed-prefix-count": "0",
                    }
                ],
                "description": "sjkGDS221-EC11",
                "flap-count": "133",
                "group-index": "11",
                "input-messages": "218603",
                "input-octets": "4153468",
                "input-refreshes": "0",
                "input-updates": "1",
                "keepalive-interval": "10",
                "last-checked": "1999159",
                "last-error": "Hold Timer Expired Error",
                "last-event": "RecvKeepAlive",
                "last-flap-event": "HoldTime",
                "last-received": "1",
                "last-sent": "3",
                "last-state": "OpenConfirm",
                "local-address": "2001:db8:223c:ca45::b+63754",
                "local-as": "65171",
                "local-ext-nh-color-nlri": "inet6-unicast",
                "nlri-type-peer": "inet6-unicast",
                "nlri-type-session": "inet6-unicast",
                "output-messages": "221174",
                "output-octets": "4202317",
                "output-refreshes": "0",
                "output-updates": "0",
                "peer-4byte-as-capability-advertised": "65151",
                "peer-addpath-not-supported": True,
                "active-holdtime": "30",
                "peer-id": "10.169.14.240",
                "local-id": "10.189.5.252",
                "peer-address": "2001:db8:eb18:ca45::1+179",
                "peer-as": "65151",
                "peer-cfg-rti": "master",
                "peer-end-of-rib-received": "inet6-unicast",
                "peer-end-of-rib-sent": "inet6-unicast",
                "peer-flags": "Sync",
                "peer-fwd-rti": "master",
                "peer-group": "v6_sjkGDS221-EC11",
                "peer-index": "0",
                "peer-no-llgr-restarter": True,
                "peer-no-restart": True,
                "peer-refresh-capability": "2",
                "peer-restart-flags-received": "Notification",
                "peer-restart-nlri-configured": "inet6-unicast",
                "peer-restart-nlri-negotiated": "inet6-unicast",
                "peer-stale-route-time-configured": "300",
                "peer-state": "Established",
                "peer-type": "External",
                "snmp-index": "16",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "obpGCS001-WC11",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:eb18:ca45::11",
                "peer-as": "65151",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_obpGCS001-WC11",
                "peer-state": "Active",
                "peer-type": "External",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_pyats201)",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "cm-hkt003",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:223c:ca45::7",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_RRC_72_TRIANGLE",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_pyats201)",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "cm-hkt004",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "ConnectRetry",
                "last-state": "Active",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:223c:ca45::8+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_RRC_72_TRIANGLE",
                "peer-state": "Connect",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "ALL_out",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "cm-hkm003",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:223c:ca45::9",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_RRC_72_SQUARE",
                "peer-state": "Active",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "ALL_out",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "cm-hkm004",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "ConnectRetry",
                "last-state": "Active",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:223c:ca45::a+179",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_RRC_72_SQUARE",
                "peer-state": "Connect",
                "peer-type": "Internal",
                "route-reflector-client": True,
            },
            {
                "bgp-bfd": {
                    "bfd-configuration-state": "disabled",
                    "bfd-operational-state": "down",
                },
                "bgp-error": [
                    {
                        "name": "Hold Timer Expired Error",
                        "receive-count": "40",
                        "send-count": "27",
                    },
                    {"name": "Cease", "receive-count": "0", "send-count": "16"},
                ],
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Preference LocalAddress HoldTime AuthKey LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "60",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "bgp-output-queue": [
                    {
                        "count": "0",
                        "number": "3",
                        "rib-adv-nlri": "inet6-unicast",
                        "table-name": "inet6.0",
                    }
                ],
                "bgp-peer-iosession": {
                    "iosession-state": "Enabled",
                    "iosession-thread-name": "bgpio-0",
                },
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "0",
                        "active-prefix-count": "0",
                        "advertised-prefix-count": "0",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet6.0",
                        "received-prefix-count": "0",
                        "rib-bit": "40001",
                        "send-state": "in sync",
                        "suppressed-prefix-count": "0",
                    }
                ],
                "description": "hktGCS002",
                "flap-count": "55",
                "group-index": "1",
                "input-messages": "110662",
                "input-octets": "2102633",
                "input-refreshes": "0",
                "input-updates": "1",
                "keepalive-interval": "20",
                "last-checked": "16510983",
                "last-error": "Hold Timer Expired Error",
                "last-event": "RecvKeepAlive",
                "last-flap-event": "HoldTime",
                "last-received": "6",
                "last-sent": "5",
                "last-state": "OpenConfirm",
                "local-address": "2001:db8:223c:ca45::b+179",
                "local-as": "65171",
                "local-ext-nh-color-nlri": "inet6-unicast",
                "nlri-type-peer": "inet6-unicast",
                "nlri-type-session": "inet6-unicast",
                "output-messages": "110664",
                "output-octets": "2102627",
                "output-refreshes": "0",
                "output-updates": "0",
                "peer-4byte-as-capability-advertised": "65171",
                "peer-addpath-not-supported": True,
                "active-holdtime": "60",
                "peer-id": "10.189.5.253",
                "local-id": "10.189.5.252",
                "peer-address": "2001:db8:223c:ca45::c+60268",
                "peer-as": "65171",
                "peer-cfg-rti": "master",
                "peer-end-of-rib-received": "inet6-unicast",
                "peer-end-of-rib-sent": "inet6-unicast",
                "peer-flags": "Sync",
                "peer-fwd-rti": "master",
                "peer-group": "v6_hktGCS002",
                "peer-index": "0",
                "peer-no-llgr-restarter": True,
                "peer-no-restart": True,
                "peer-refresh-capability": "2",
                "peer-restart-flags-received": "Notification",
                "peer-restart-nlri-configured": "inet6-unicast",
                "peer-restart-nlri-negotiated": "inet6-unicast",
                "peer-stale-route-time-configured": "300",
                "peer-state": "Established",
                "peer-type": "Internal",
                "snmp-index": "1",
            },
            {
                "bgp-option-information": {
                    "authentication-configured": True,
                    "bgp-options": "Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed",
                    "bgp-options-extended": "GracefulShutdownRcv",
                    "bgp-options2": True,
                    "export-policy": "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                    "gshut-recv-local-preference": "0",
                    "holdtime": "30",
                    "local-address": "2001:db8:223c:ca45::b",
                    "preference": "170",
                },
                "description": "sggjbb001",
                "flap-count": "0",
                "last-error": "None",
                "last-event": "Start",
                "last-state": "Idle",
                "local-address": "2001:db8:223c:ca45::b",
                "local-as": "65171",
                "peer-address": "2001:db8:5961:ca45::1",
                "peer-as": "65181",
                "peer-cfg-rti": "master",
                "peer-flags": "",
                "peer-fwd-rti": "master",
                "peer-group": "v6_sggjbb001",
                "peer-state": "Active",
                "peer-type": "External",
            },
        ]
    }
}
