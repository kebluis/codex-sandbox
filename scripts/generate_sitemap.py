import os
import xml.etree.ElementTree as ET
import datetime

repo = os.getenv('GITHUB_REPOSITORY', '')
owner_repo = repo.split('/') if repo else ['','']
owner, repo_name = (owner_repo + ['', ''])[:2]
base_url = os.getenv('SITE_URL') or f'https://{owner}.github.io/{repo_name}'

html_files = []
for root, dirs, files in os.walk('.', topdown=True):
    # skip .git directory
    if '.git' in dirs:
        dirs.remove('.git')
    if '.github' in dirs:
        dirs.remove('.github')
    for fname in files:
        if fname.endswith('.html'):
            path = os.path.relpath(os.path.join(root, fname), '.')
            if path == 'sitemap.xml':
                continue
            html_files.append(path)

urlset = ET.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for path in sorted(html_files):
    url = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(url, 'loc')
    loc.text = f'{base_url}/{path}'
    lastmod = ET.SubElement(url, 'lastmod')
    lastmod.text = datetime.date.today().isoformat()

ET.ElementTree(urlset).write('sitemap.xml', encoding='utf-8', xml_declaration=True)
print('Generated sitemap.xml with', len(html_files), 'entries')
