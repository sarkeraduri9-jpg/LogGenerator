import yaml

domains = {
    "database": ["MYSQL", "ORACLE", "POSTGRES", "MONGODB"],
    "jvm": ["MEM", "GC", "THREAD", "CLASSLOADER"],
    "network": ["SOCK", "DNS", "TIMEOUT", "SSL"],
    "application": ["SPRING", "HIBERNATE", "KAFKA", "REST"],
    "os": ["LINUX", "DISK", "CPU", "MEMORY"]
}

errors = {
    "version": "1.1",
    "error_domains": {}
}

counter = 1

for domain, subsystems in domains.items():
    errors["error_domains"][domain] = {}
    for sub in subsystems:
        rules = []
        for i in range(1, 501):  # 500 rules per subsystem
            rule = {
                "error_code": f"{domain[:3].upper()}-{sub}-{i:04}",
                "severity": ["LOW", "MEDIUM", "HIGH", "CRITICAL"][i % 4],
                "regex_patterns": [
                    f"{sub} error {i}",
                    f"{sub} failure {i}"
                ],
                "description": f"Auto-generated {sub} error {i}",
                "action": "Refer system runbook"
            }
            rules.append(rule)
            counter += 1
        errors["error_domains"][domain][sub.lower()] = rules

with open("error_signatures.yaml", "w") as f:
    yaml.dump(errors, f, sort_keys=False)

print("Generated error_signatures.yaml with 10,000+ rules")
