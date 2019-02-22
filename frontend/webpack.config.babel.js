const path = require('path')
const { VueLoaderPlugin } = require('vue-loader')
const HtmlWebpackPlugin = require('html-webpack-plugin')
// const MiniCssExtractPlugin = require('mini-css-extract-plugin')
// const StyleLintPlugin = require('stylelint-webpack-plugin')
const nodeSassMagicImporter = require('node-sass-magic-importer');

// const CleanWebpackPlugin = require('clean-webpack-plugin')
require('babel-polyfill')

const repoRoot = __dirname
const appRoot = path.join(repoRoot, 'app')
const distRoot = path.join(repoRoot, 'dist')
const publicRoot = path.join(repoRoot, 'public')


module.exports = (env, argv) => {
    const mode = argv ? argv.mode : 'development'

    let isProd = () => {
        return mode !== 'development'
    }

    let plugins = [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            title: 'vue-auth',
            template: path.join(publicRoot, 'index.html'),
        }),
        // new MiniCssExtractPlugin({
        //     filename: '[name].css',
        //     chunkFilename: '[id].css',
        // }),
        // new StyleLintPlugin({
        //     files: ['**/*.{vue,htm,html,css,scss,sass}'],
        // }),
    ]

    if (isProd()) {
        plugins = [
            // new CleanWebpackPlugin([distRoot]),
            ...plugins,
        ]
    }

    return {
        context: appRoot,

        output: {
            path: distRoot,
            filename: '[name].[hash].js',
            chunkFilename: '[name].[chunkhash].js',
            publicPath: '/',
        },

        plugins: plugins,

        entry: {
            index: ['babel-polyfill', path.join(appRoot, 'index.js')],
            vendor: [
                'vue', 'vuex', 'vee-validate', 'axios', 'lodash/template', 'lodash/orderBy',
                'vue-router', 'vue-i18n', 'humps',
            ],
        },
        resolve: {
            modules: [
                appRoot,
                'node_modules',
            ],
            extensions: ['*', '.js', '.vue', '.json'],
        },
        optimization: {
            splitChunks: {
                cacheGroups: {
                    vendor: {
                        chunks: 'initial',
                        name: 'vendor',
                        test: 'vendor',
                        enforce: true,
                    },
                },
            },
            runtimeChunk: true,
        },
        module: {
            rules: [
                {
                    test: /\.(js|vue)$/,
                    use: 'eslint-loader',
                    exclude: /node_modules/,
                    enforce: 'pre',
                },
                {
                    test: /\.js$/,
                    use: 'babel-loader',
                    include: [appRoot],
                },
                {
                    test: /\.vue$/,
                    use: 'vue-loader',
                },
                {
                    test: /\.(sa|sc|c)ss$/,
                    use: [
                        'vue-style-loader',
                        'css-loader',
                        'postcss-loader',
                        {
                            loader: 'sass-loader',
                            options: {
                                importer: nodeSassMagicImporter(),
                            },
                        },
                    ],
                },
            ],
        },
        devtool: isProd() ? false : '#eval-source-map',
        devServer: {
            host: '0.0.0.0',
            port: '9010',
            disableHostCheck: true,
            historyApiFallback: true,
            watchOptions: {
                poll: true,
            },
        },
    }
}
