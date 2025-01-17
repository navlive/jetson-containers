
from jetson_containers import L4T_VERSION

if L4T_VERSION.major >= 34:
    package['depends'].extend(['bitsandbytes', 'auto_gptq'])

    # version installed from source
    package_git = package.copy()
    
    package_git['name'] = 'transformers:git'
    
    package_git['build_args'] = {
        'TRANSFORMERS_PACKAGE': "git+https://github.com/huggingface/transformers",
        'TRANSFORMERS_VERSION': "https://api.github.com/repos/huggingface/transformers/git/refs/heads/main"
    }
    
    # version with nvgpt support
    package_nvgpt = package.copy()
    
    package_nvgpt['name'] = 'transformers:nvgpt'
    
    package_nvgpt['build_args'] = {
        'TRANSFORMERS_PACKAGE': "git+https://github.com/ertkonuk/transformers",
        'TRANSFORMERS_VERSION': "https://api.github.com/repos/ertkonuk/transformers/git/refs/heads/main"
    }
    
    package = [package, package_git, package_nvgpt]