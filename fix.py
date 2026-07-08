import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Avatar linkini guncelle (eski hash bozuktu)
old_avatar = 'https://cdn.discordapp.com/avatars/931547111865085952/a_a4eee08b2a44525a547f5642a3892b18.gif?size=4096'
new_avatar = 'https://cdn.discordapp.com/avatars/931547111865085952/a03a042296661e0487c639f766fbfda6.png?size=4096'
content = content.replace(old_avatar, new_avatar)

# 2. Discord butonu - ikon + kucuk modern hali
old_btn = '<a class="discord-btn" href="https://discord.com/users/931547111865085952" target="_blank" rel="noopener">ADD ME ON DISCORD</a>'
new_btn = '<a class="discord-btn" href="https://discord.com/users/931547111865085952" target="_blank" rel="noopener"><svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M20.317 4.37a19.79 19.79 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.056 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128c.126-.094.252-.192.372-.291a.074.074 0 0 1 .077-.01c3.927 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.099.246.197.373.291a.077.077 0 0 1-.006.128 12.3 12.3 0 0 1-1.873.892.076.076 0 0 0-.041.106c.36.699.772 1.364 1.225 1.994a.077.077 0 0 0 .084.028 19.84 19.84 0 0 0 6.002-3.03.077.077 0 0 0 .032-.055c.5-5.177-.838-9.673-3.549-13.66a.06.06 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.418 2.157-2.418 1.21 0 2.176 1.094 2.157 2.418 0 1.334-.955 2.419-2.157 2.419zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.418 2.157-2.418 1.21 0 2.175 1.094 2.157 2.418 0 1.334-.947 2.419-2.157 2.419z"/></svg>Add me on Discord</a>'
if old_btn in content:
    content = content.replace(old_btn, new_btn)
    print("Buton HTML degisti: OK")
else:
    print("UYARI: buton HTML eslesmedi, elle kontrol")

# 3. CSS - buton kucuk ve modern
content, n1 = re.subn(
    r'\.discord-btn\s*\{[^}]*\}',
    '''.discord-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin: 8px auto 2px;
  padding: 5px 12px;
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 1px;
  color: rgba(255,255,255,.8);
  background: rgba(88, 101, 242, 0.15);
  border: 1px solid rgba(88, 101, 242, 0.4);
  border-radius: 14px;
  text-decoration: none;
  cursor: pointer;
  backdrop-filter: blur(6px);
  transition: background .2s, border-color .2s, transform .15s;
}''', content, count=1)
content, n2 = re.subn(
    r'\.discord-btn:hover\s*\{[^}]*\}',
    '''.discord-btn:hover {
  background: rgba(88, 101, 242, 0.3);
  border-color: rgba(88, 101, 242, 0.7);
  transform: translateY(-1px);
}''', content, count=1)
print(f"CSS degisti: discord-btn={n1}, hover={n2}")

# 4. Survive Homelanders otomatik yonlendirmeyi kaldir
old_card = '''<a href="https://discord.gg/survivehl" target="_blank" class="project-link">
              <div class="project-card animate-slide" style="cursor: pointer;" data-invite="survivehl">
                <div class="game-title">Survival Homelanders</div>
                <div class="game-role">Moderator</div>
                <div class="game-stats">Loading stats...</div>
              </div>
            </a>'''
new_card = '''<div class="project-card animate-slide" data-invite="survivehl">
              <div class="game-title">Survival Homelanders</div>
              <div class="game-role">Moderator</div>
              <div class="game-stats">Loading stats...</div>
            </div>'''
if old_card in content:
    content = content.replace(old_card, new_card)
    print("Survive Homelanders linki kaldirildi: OK")
else:
    print("UYARI: Survive Homelanders blogu eslesmedi, elle kontrol")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
