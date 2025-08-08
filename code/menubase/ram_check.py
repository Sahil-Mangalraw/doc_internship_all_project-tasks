import psutil
import platform
import time

def get_ram_info():
    """Get detailed RAM information"""
    print("=" * 50)
    print("💾 RAM USAGE INFORMATION")
    print("=" * 50)
    
    # Get memory information
    memory = psutil.virtual_memory()
    
    print(f"📊 Total RAM: {memory.total / (1024**3):.2f} GB")
    print(f"📊 Available RAM: {memory.available / (1024**3):.2f} GB")
    print(f"📊 Used RAM: {memory.used / (1024**3):.2f} GB")
    print(f"📊 RAM Usage Percentage: {memory.percent:.1f}%")
    
    # Get swap memory information
    swap = psutil.swap_memory()
    print(f"\n💿 Swap Memory:")
    print(f"   Total: {swap.total / (1024**3):.2f} GB")
    print(f"   Used: {swap.used / (1024**3):.2f} GB")
    print(f"   Free: {swap.free / (1024**3):.2f} GB")
    print(f"   Usage: {swap.percent:.1f}%")
    
    # System information
    print(f"\n🖥️ System Information:")
    print(f"   OS: {platform.system()} {platform.release()}")
    print(f"   Architecture: {platform.machine()}")
    print(f"   Processor: {platform.processor()}")
    
    # Memory status
    if memory.percent < 50:
        print(f"\n✅ RAM usage is healthy ({memory.percent:.1f}%)")
    elif memory.percent < 80:
        print(f"\n⚠️ RAM usage is moderate ({memory.percent:.1f}%)")
    else:
        print(f"\n🚨 RAM usage is high ({memory.percent:.1f}%) - Consider closing some applications")
    
    print("=" * 50)

if __name__ == "__main__":
    try:
        get_ram_info()
    except ImportError:
        print("❌ psutil module not found. Installing...")
        import subprocess
        subprocess.check_call(["pip", "install", "psutil"])
        print("✅ psutil installed successfully!")
        get_ram_info()
    except Exception as e:
        print(f"❌ Error: {e}") 