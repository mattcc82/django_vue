const BundleTracker = require('webpack-bundle-tracker')
// https://github.com/owais/webpack-bundle-tracker

module.exports = {
  // windows - user localhost or 127.0.0.1
  // https://cli.vuejs.org/config/#publicpath
  // https://cli.vuejs.org/config/#outputdir
  publicPath: 'http://127.0.0.1:8080/',
  outputDir: './dist/',

  // https://cli.vuejs.org/guide/webpack.html#chaining-advanced
  chainWebpack: config => {
    // https://webpack.js.org/concepts/plugins/#root
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: './webpack-stats.json' }])

    // https://webpack.js.org/concepts/output/#root
    config.output
      .filename('bundle.js')

    // https://webpack.js.org/configuration/optimization/#optimizationsplitchunks
    config.optimization
      .splitChunks(false)

    // https://webpack.js.org/configuration/resolve/#resolvealias
    config.resolve.alias
      .set('__STATIC__', 'static')

    // https://webpack.js.org/configuration/dev-server/
    config.devServer
      .public('http://127.0.0.1:8080')
      .host('127.0.0.1')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      // eslint-disable-next-line no-useless-escape
      .headers({ 'Access-Control-Allow-Origin': ['\*'] })
  // eslint-disable-next-line comma-dangle
  },
  css: {
    extract: {
      filename: 'bundle.css',
      chunkFilename: 'bundle.css'
    }
  }
}
