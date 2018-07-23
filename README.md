# AnnotateSystem

Django + Vue + Webpack

## install

```bash
cd appfront
npm install
```

```bash
pip install webpack_loader
pip install django-cors-headers
```

### settings.py

```python
INSTALLED_APPS

'corsheaders.middleware.CorsMiddleware',

CORS_ORIGIN_WHITELIST = (
'localhost:8080',
) | CORS_ORIGIN_ALLOW_ALL = True

CSRF_COOKIE_NAME = "XSRF-TOKEN"

# Add for vuejs

STATICFILES_DIRS = [
os.path.join(BASE_DIR, "appfront/dist/static"),
]

WEBPACK_LOADER = {
'DEFAULT': {
'BUNDLE_DIR_NAME': 'dist/',
'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
}
}

- dev
  TEMPLATES
  'DIRS': [os.path.join(BASE_DIR, 'annotate/templates')],
- prod
  'DIRS': ['appfront/dist'],
   # 同时更改 urls.py 路由
```

### dev

- build/webpack.dev.conf.js

  - `devServer: -> plugin`

    ```python
    // generate webpack-stats.json using Webpack plugin webpack-bundle-tracker
    new BundleTracker({filename: '../webpack-stats.json'})
    ```

- config/index.js

```python
dev: {
    // Paths
    assetsSubDirectory: 'static',
    // assetsPublicPath: '/',
    assetsPublicPath: 'http://localhost:8080/',
    proxyTable: {},

    // Various Dev Server settings
    host: 'localhost', // can be overwritten by process.env.HOST
    port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    # ...
```

### build

```bash
    npm run build
```

### main.js

```js
import axios from "axios";
let host = window.location.host.split(":")[0];
axios.defaults.baseURL = `http://${host}:9006`;
// CSRF
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";
Vue.prototype.$axios = axios;
```
