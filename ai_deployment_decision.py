import random
import subprocess

def ai_deploy_decision():
    # Run Snyk security scan
    snyk_check = subprocess.run(['snyk', 'test'], capture_output=True, text=True)
    
    # If Snyk finds vulnerabilities, reject deployment
    if "issues found" in snyk_check.stdout:
        print("Security vulnerabilities found. Deployment rejected.")
        return 'reject'
    
    # Otherwise, make a random decision (for demo purposes)
    decision = random.choice(['deploy', 'reject'])
    return decision

if ai_deploy_decision() == 'deploy':
    print("Deployment approved.")
else:
    print("Deployment rejected. Fix issues and try again.")
