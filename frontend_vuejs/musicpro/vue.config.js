const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})


module.exports = {
  devServer: {
    proxy: {
      '^/listproducts': {
        target: 'http://127.0.0.1:5000',
        ws: true,
        changeOrigin: true
      },
      '^/login2': {
        target: 'http://127.0.0.1:5000',
        ws: true,
        changeOrigin: true
      },
      '^/updateShoppingCart': {
        target: 'http://127.0.0.1:5000',
        ws: true,
        changeOrigin: true
      },
    }
  }
}
