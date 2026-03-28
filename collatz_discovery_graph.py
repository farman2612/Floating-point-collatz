import matplotlib.pyplot as plt

# 1. Your Custom Collatz Logic
def test_collatz_decimal(n):
    original = int(n)       
    final = n - original
    if final > 0.5:
        if original % 2 == 0:
            return (n * 3) + 1
        else:
            return n / 2   
    else:
        if original % 2 == 0:
           return n / 2 
        else:
            return (n * 3) + 1

# 2. Generate the Data
steps = 15
stable_num = 15.5001 # Microscopic deviation (collapses to loop)
divergent_num = 15.5 # Edge case (explodes to infinity)

stable_seq = [stable_num]
divergent_seq = [divergent_num]

for _ in range(steps):
    stable_num = test_collatz_decimal(stable_num)
    stable_seq.append(stable_num)
    
    divergent_num = test_collatz_decimal(divergent_num)
    divergent_seq.append(divergent_num)

# 3. Create the Visual Infographic
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Floating-Point Collatz: Attractors vs. Divergence', fontsize=18, fontweight='bold', color='white')

# Left Chart: The Stable Loop
ax1.plot(stable_seq, marker='o', color='#00ffcc', linewidth=2, markersize=6)
ax1.set_title('Stable Attractor (Input: 15.5001)', fontsize=14, pad=15)
ax1.set_xlabel('Steps', fontsize=12)
ax1.set_ylabel('Value', fontsize=12)
ax1.grid(True, alpha=0.2)
ax1.annotate('Collapses into 4-2-1 loop', xy=(8, 4), xytext=(5, 10),
             arrowprops=dict(facecolor='white', shrink=0.05), fontsize=11)

# Right Chart: The Infinite Divergence (Log Scale)
ax2.plot(divergent_seq, marker='o', color='#ff3366', linewidth=2, markersize=6)
ax2.set_title('Infinite Divergence (Input: 15.5)', fontsize=14, pad=15)
ax2.set_xlabel('Steps', fontsize=12)
ax2.set_ylabel('Value (Log Scale)', fontsize=12)
ax2.set_yscale('log') # Log scale is required because it explodes!
ax2.grid(True, alpha=0.2)
ax2.annotate('Explodes to Infinity', xy=(12, divergent_seq[12]), xytext=(2, divergent_seq[12]),
             arrowprops=dict(facecolor='white', shrink=0.05), fontsize=11)

# Format and Save
plt.tight_layout()
fig.subplots_adjust(top=0.85)
plt.savefig('collatz_discovery.png', dpi=300, bbox_inches='tight')
print("Image successfully saved as 'collatz_discovery.png'!")
plt.show()
