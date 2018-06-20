service {
    ssh {
        port 22
    }
}
system {
    host-name vyos
    login {
        user vyos {
            authentication {
                encrypted-password "$6$MjV2YvKQ56q$QbL562qhRoyUu8OaqrXagicvcsNpF1HssCY06ZxxghDJkBCfSfTE/4FlFB41xZcd/HqYyVBuRt8Zyq3ozJ0dc."
                plaintext-password ""
            }
            level admin
        }
    }
    syslog {
        global {
            facility all {
                level notice
            }
            facility protocols {
                level debug
            }
        }
    }
    ntp {
        server "0.pool.ntp.org"
        server "1.pool.ntp.org"
        server "2.pool.ntp.org"
    }
    config-management {
        commit-revisions 100
    }
}
interfaces {
    ethernet eth0 {
        address dhcp
    }
    loopback lo
}
